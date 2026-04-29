-- Добавление телефона к существующему контакту
CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name;
    IF v_contact_id IS NOT NULL THEN
        INSERT INTO phones (contact_id, phone, type) VALUES (v_contact_id, p_phone, p_type);
    END IF;
END;
$$;

-- Смена группы контакта
CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_group_id INT;
BEGIN
    INSERT INTO groups (name) VALUES (p_group_name) ON CONFLICT (name) DO NOTHING;
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    
    UPDATE contacts SET group_id = v_group_id WHERE name = p_contact_name;
END;
$$;

-- Расширенный поиск по всем полям
CREATE OR REPLACE FUNCTION search_contacts_extended(p_query TEXT)
RETURNS TABLE(contact_id INT, name VARCHAR, email VARCHAR, phones_list TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email, string_agg(p.phone  '('  p.type  ')', ', ')
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%'  p_query  '%'
       OR c.email ILIKE '%'  p_query  '%'
       OR p.phone ILIKE '%'  p_query || '%'
    GROUP BY c.id, c.name, c.email;
END;
$$ LANGUAGE plpgsql;